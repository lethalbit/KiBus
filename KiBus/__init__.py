try:
    # Note the relative import!
    from .action_kibus import KiBus
    # Instantiate and register to Pcbnew
    KiBus().register()
except Exception as e:
    from pathlib import Path

    kibus_path = Path(__file__).resolve().parent
    log_file = kibus_path / 'kibus_error.log'

    with log_file.open('w') as f:
        f.write(repr(e))
