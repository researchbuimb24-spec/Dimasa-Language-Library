"""Unit tests for Dimasa Cultural Heritage Database."""

import pytest
import dimasa


def test_cultural_attire():
    attire_list = dimasa.list_attire()
    assert len(attire_list) >= 5
    ids = [a["id"] for a in attire_list]
    assert "rigu" in ids
    assert "rikhaosa" in ids
    assert "rigdo" in ids
    assert "bathormai" in ids
    assert "sgaopha" in ids

    rigu = dimasa.get_attire("rigu")
    assert rigu is not None
    assert "skirt" in rigu["description"].lower()


def test_cultural_festivals():
    festivals = dimasa.list_festivals()
    assert len(festivals) >= 3
    ids = [f["id"] for f in festivals]
    assert "bushu_dima" in ids
    assert "rajini_gabra" in ids

    bushu = dimasa.get_festival("bushu_dima")
    assert bushu is not None
    assert "thanksgiving" in bushu["description"].lower()
    types = [t["name"] for t in bushu["types"]]
    assert "Hangseu Bushu" in types
    assert "Surem Bushu" in types
    assert "Jidab Bushu" in types


def test_cultural_clans_and_marriage_compatibility():
    clans_data = dimasa.list_clans()
    sengphongs = clans_data.get("sengphongs", [])
    julus = clans_data.get("julus", [])

    # Exact authentic clan counts
    assert len(sengphongs) == 40
    assert len(julus) >= 10

    sp_names = [sp["name"] for sp in sengphongs]
    assert "Langthasa" in sp_names
    assert "Thaosen" in sp_names
    assert "Hagjer" in sp_names
    assert "Hojai" in sp_names

    # Test double-exogamy marriage compatibility checker
    # Prohibited 1: Same Sengphong
    compat1, msg1 = dimasa.check_marriage_compatibility("Langthasa", "Maireng", "Langthasa", "Saidima")
    assert compat1 is False
    assert "Sengphong" in msg1

    # Prohibited 2: Same Julu
    compat2, msg2 = dimasa.check_marriage_compatibility("Langthasa", "Maireng", "Thaosen", "Maireng")
    assert compat2 is False
    assert "Julu" in msg2

    # Allowed: Different Sengphong AND Different Julu
    compat3, msg3 = dimasa.check_marriage_compatibility("Langthasa", "Maireng", "Thaosen", "Saidima")
    assert compat3 is True
    assert "Compatible" in msg3


def test_cultural_cuisine():
    dishes = dimasa.list_dishes()
    assert len(dishes) >= 4
    dish_ids = [d["id"] for d in dishes]
    assert "judima" in dish_ids
    assert "napham" in dish_ids
    assert "gundru" in dish_ids
    assert "khar" in dish_ids

    judima = dimasa.get_dish("judima")
    assert judima is not None
    assert "Thembra" in judima["ingredients"][1]


def test_cultural_places():
    places = dimasa.list_places()
    assert len(places) >= 4
    place_ids = [p["id"] for p in places]
    assert "dima_hasao" in place_ids
    assert "dimapur" in place_ids
    assert "maibang" in place_ids
    assert "khaspur" in place_ids


def test_cultural_idioms():
    idioms = dimasa.list_idioms()
    assert len(idioms) >= 3
    assert any("di ring-ba" in i["dimasa"] for i in idioms)


def test_cultural_instruments():
    instruments = dimasa.list_instruments()
    assert len(instruments) >= 3
    inst_ids = [i["id"] for i in instruments]
    assert "khram" in inst_ids
    assert "muri" in inst_ids

