APP_TITLE = "Crop My GIF v1.3"
FILE_INPUT = 'Select a GIF to crop'
START_TOOLTIP = "Load GIF file animation"
BROWSE_TOOLTIP = "Select a GIF file"
GIF_TYPE = (('GIF file', '*.gif *.GIF'),)
DEFAULT_INFO = 'Click GIF'
SELECT_FRAME = "SELECTED GIF AREA"
CROP_FRAME = "CROP MY GIF"
RESET_BTN = "Clear Selection"
CROP_BTN = "Crop My GIF"
PRESERVE_CHECK = 'Preserve FPS'
PRESERVE_FPS_TOOLTIP = (
    f'If checked, the crop GIF file will have\n'
    f'the same frame rate as the input.\n\n'
    f'Takes longer to export.'
)
PROGRESS_TITLE = (
    'Exporting cropped GIF file...',
    'Loading GIF animation...'
)
def PROGRESS_MSG(n_frames=0):
    if n_frames:
        return f'Loading {n_frames} GIF frames'
    return 'Exporting cropped GIF file...'
EXPORTED_MSG = (f'\nCropped GIF exported!\n'
                f'Would you like to open it?\n')
