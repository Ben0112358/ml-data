def test_config_paths_resolve(ml_data_env):
    import ml_data.config as config

    assert config.RAW_DATA_DIR.name == "raw"
    assert config.CLEAN_DATA_DIR.name == "clean"
