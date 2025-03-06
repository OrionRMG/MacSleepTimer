# The PEP 484 type hints stub file for the QtMacExtras module.
#
# Generated by SIP 6.8.6
#
# Copyright (c) 2024 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

import PyQt5.sip

from PyQt5 import QtCore
from PyQt5 import QtGui

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        PyQt5.sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], PyQt5.sip.Buffer, int, None]


class QMacPasteboardMime(PyQt5.sipsimplewrapper):

    class QMacPasteboardMimeType(int):
        MIME_DND = ... # type: QMacPasteboardMime.QMacPasteboardMimeType
        MIME_CLIP = ... # type: QMacPasteboardMime.QMacPasteboardMimeType
        MIME_QT_CONVERTOR = ... # type: QMacPasteboardMime.QMacPasteboardMimeType
        MIME_QT3_CONVERTOR = ... # type: QMacPasteboardMime.QMacPasteboardMimeType
        MIME_ALL = ... # type: QMacPasteboardMime.QMacPasteboardMimeType

    @typing.overload
    def __init__(self, t: int) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QMacPasteboardMime') -> None: ...

    def count(self, mimeData: typing.Optional[QtCore.QMimeData]) -> int: ...
    def convertFromMime(self, mime: typing.Optional[str], data: typing.Any, flav: typing.Optional[str]) -> typing.List[QtCore.QByteArray]: ...
    def convertToMime(self, mime: typing.Optional[str], data: typing.Iterable[typing.Union[QtCore.QByteArray, bytes, bytearray]], flav: typing.Optional[str]) -> typing.Any: ...
    def flavorFor(self, mime: typing.Optional[str]) -> str: ...
    def mimeFor(self, flav: typing.Optional[str]) -> str: ...
    def canConvert(self, mime: typing.Optional[str], flav: typing.Optional[str]) -> bool: ...
    def convertorName(self) -> str: ...


class NSToolbar(PyQt5.sipsimplewrapper): ...


class QMacToolBar(QtCore.QObject):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, identifier: typing.Optional[str], parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def nativeToolbar(self) -> typing.Optional[NSToolbar]: ...
    def detachFromWindow(self) -> None: ...
    def attachToWindow(self, window: typing.Optional[QtGui.QWindow]) -> None: ...
    def allowedItems(self) -> typing.List['QMacToolBarItem']: ...
    def setAllowedItems(self, allowedItems: typing.Iterable['QMacToolBarItem']) -> None: ...
    def items(self) -> typing.List['QMacToolBarItem']: ...
    def setItems(self, items: typing.Iterable['QMacToolBarItem']) -> None: ...
    def addSeparator(self) -> None: ...
    def addAllowedItem(self, icon: QtGui.QIcon, text: typing.Optional[str]) -> typing.Optional['QMacToolBarItem']: ...
    def addItem(self, icon: QtGui.QIcon, text: typing.Optional[str]) -> typing.Optional['QMacToolBarItem']: ...


class NSToolbarItem(PyQt5.sipsimplewrapper): ...


class QMacToolBarItem(QtCore.QObject):

    class StandardItem(int):
        NoStandardItem = ... # type: QMacToolBarItem.StandardItem
        Space = ... # type: QMacToolBarItem.StandardItem
        FlexibleSpace = ... # type: QMacToolBarItem.StandardItem

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    activated: typing.ClassVar[QtCore.pyqtSignal]
    def nativeToolBarItem(self) -> typing.Optional[NSToolbarItem]: ...
    def setIcon(self, icon: QtGui.QIcon) -> None: ...
    def icon(self) -> QtGui.QIcon: ...
    def setText(self, text: typing.Optional[str]) -> None: ...
    def text(self) -> str: ...
    def setStandardItem(self, standardItem: 'QMacToolBarItem.StandardItem') -> None: ...
    def standardItem(self) -> 'QMacToolBarItem.StandardItem': ...
    def setSelectable(self, selectable: bool) -> None: ...
    def selectable(self) -> bool: ...


class QtMac(PyQt5.sip.simplewrapper):

    def isMainWindow(self, window: typing.Optional[QtGui.QWindow]) -> bool: ...
    def badgeLabelText(self) -> str: ...
    def setBadgeLabelText(self, text: typing.Optional[str]) -> None: ...


def qRegisterDraggedTypes(types: typing.Iterable[typing.Optional[str]]) -> None: ...
