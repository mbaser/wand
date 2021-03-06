""":mod:`wand.cdefs.magick_property` --- Magick-Property definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.5.0
"""
from ctypes import (POINTER, c_void_p, c_char_p, c_size_t, c_uint, c_int,
                    c_double)
from wand.cdefs.wandtypes import c_magick_char_p

__all__ = ('load',)


def load(lib, IM_VERSION):
    """Define Magick Wand property methods. The ImageMagick version is given as
    a second argument for comparison. This will quick to determine which
    methods are available from the library, and can be implemented as::

        if IM_VERSION < 0x700:
            # ... do ImageMagick-6 methods ...
        else
            # ... do ImageMagick-7 methods ...

    .. seealso::

        #include "wand/magick-property.h"
        // Or
        #include "MagickWand/magick-property.h"

    :param lib: the loaded ``MagickWand`` library
    :type lib: :class:`ctypes.CDLL`
    :param IM_VERSION: the ImageMagick version number (i.e. 0x0689)
    :type IM_VERSION: :class:`numbers.Integral`

    .. versionadded:: 0.5.0

    """
    lib.MagickDeleteImageProperty.argtypes = [c_void_p, c_char_p]
    lib.MagickDeleteOption.argtypes = [c_void_p, c_char_p]
    lib.MagickDeleteOption.restype = c_int
    lib.MagickGetAntialias.argtypes = [c_void_p]
    lib.MagickGetAntialias.restype = c_int
    lib.MagickGetBackgroundColor.argtypes = [c_void_p]
    lib.MagickGetBackgroundColor.restype = c_void_p
    lib.MagickGetFont.argtypes = [c_void_p]
    lib.MagickGetFont.restype = c_char_p
    lib.MagickGetGravity.argtypes = [c_void_p]
    lib.MagickGetGravity.restype = c_int
    lib.MagickGetImageArtifact.argtypes = [c_void_p, c_char_p]
    lib.MagickGetImageArtifact.restype = c_magick_char_p
    lib.MagickGetImageArtifacts.argtypes = [
        c_void_p, c_char_p, POINTER(c_size_t)
    ]
    lib.MagickGetImageArtifacts.restype = POINTER(c_char_p)

    lib.MagickGetImageProperty.argtypes = [c_void_p, c_char_p]
    lib.MagickGetImageProperty.restype = c_magick_char_p
    lib.MagickGetImageProperties.argtypes = [
        c_void_p, c_char_p, POINTER(c_size_t)
    ]
    lib.MagickGetImageProperties.restype = POINTER(c_char_p)
    lib.MagickGetOption.argtypes = [c_void_p, c_char_p]
    lib.MagickGetOption.restype = c_char_p
    lib.MagickGetPointsize.argtypes = [c_void_p]
    lib.MagickGetPointsize.restype = c_double
    lib.MagickGetQuantumRange.argtypes = [POINTER(c_size_t)]
    lib.MagickGetSize.argtypes = [c_void_p, POINTER(c_uint), POINTER(c_uint)]
    lib.MagickGetSize.restype = c_int
    lib.MagickQueryConfigureOption.argtypes = [c_char_p]
    lib.MagickQueryConfigureOption.restype = c_magick_char_p
    lib.MagickQueryConfigureOptions.argtypes = [c_char_p, POINTER(c_size_t)]
    lib.MagickQueryConfigureOptions.restype = POINTER(c_magick_char_p)
    lib.MagickQueryFontMetrics.argtypes = [c_void_p, c_void_p, c_char_p]
    lib.MagickQueryFontMetrics.restype = POINTER(c_double)
    lib.MagickQueryFonts.argtypes = [c_char_p, POINTER(c_size_t)]
    lib.MagickQueryFonts.restype = POINTER(c_magick_char_p)
    lib.MagickQueryFormats.argtypes = [c_char_p, POINTER(c_size_t)]
    lib.MagickQueryFormats.restype = POINTER(c_magick_char_p)
    lib.MagickQueryMultilineFontMetrics.argtypes = [
        c_void_p, c_void_p, c_char_p
    ]
    lib.MagickQueryMultilineFontMetrics.restype = POINTER(c_double)
    lib.MagickSetAntialias.argtypes = [c_void_p, c_int]
    lib.MagickSetAntialias.restype = c_int
    lib.MagickSetBackgroundColor.argtypes = [c_void_p, c_void_p]
    lib.MagickSetBackgroundColor.restype = c_int
    lib.MagickSetDepth.argtypes = [c_void_p, c_uint]
    lib.MagickSetDepth.restype = c_int
    lib.MagickSetFilename.argtypes = [c_void_p, c_char_p]
    lib.MagickSetFont.argtypes = [c_void_p, c_char_p]
    lib.MagickSetFont.restype = c_int
    lib.MagickSetFormat.argtypes = [c_void_p, c_char_p]
    lib.MagickSetFormat.restype = c_int
    lib.MagickSetGravity.argtypes = [c_void_p, c_int]
    lib.MagickSetGravity.restype = c_int
    lib.MagickSetImageArtifact.argtypes = [c_void_p, c_char_p, c_char_p]
    lib.MagickSetImageProperty.argtypes = [c_void_p, c_char_p, c_char_p]
    lib.MagickSetOption.argtypes = [c_void_p, c_char_p, c_char_p]
    lib.MagickSetOption.restype = c_int
    lib.MagickSetPointsize.argtypes = [c_void_p, c_double]
    lib.MagickSetPointsize.restype = c_int
    lib.MagickSetSize.argtypes = [c_void_p, c_uint, c_uint]
    lib.MagickSetSize.restype = c_int
