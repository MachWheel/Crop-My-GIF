SELECT_FILE = 'Select a GIF to crop'
BROWSE_TITLE = 'Browse GIF'
GIF_EXTENSION = ('GIF', '*.gif')
MAIN_TITLE = "Crop My GIF"
EXPORTING_TITLE = 'Exporting cropped GIF file...'
DEFAULT_INFO = 'Click GIF'
SELECT_FRAME = "SELECTED GIF AREA"
CROP_FRAME = "CROP MY GIF"
RESET_BTN = "Clear Selection"
CROP_BTN = "CROP GIF"
PRESERVE_CHECK = 'Preserve FPS'
PRESERVE_FPS_TOOLTIP = (
    f'If checked, the crop GIF file will have\n'
    f'the same frame rate as the input.\n\n'
    f'Takes longer to export.'
)
def IMPORTING_MSG(n_frames: int): return f'Loading {n_frames} GIF frames'
EXPORTING_MSG = 'Exporting cropped GIF file...'
EXPORTED_MSG = (f'Cropped GIF exported!\n'
                f'Would you like to open it?')
