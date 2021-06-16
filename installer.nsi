;;; Comments beginning with ";;;" are commentary added by PyTom to 
;;; try to help you understand this file.
;;;
;;; This installer expects that you will have supplied LICENSE.txt 
;;; and README.txt files in the root directory of your game.
;;;
;;; To use this, place it in the root directory of your game, 
;;; right-click on it, and choose "Compile NSIS script..."

;;; First up, change the settings below to match your game.

;;; The exe used to run your game.
!define EXE "OurPersonalSpace.exe"

;;; The exe containing the installer. This will be created in the directory
;;; above the root directory containing your game. 
!define INSTALLER_EXE "OurPersonalSpace-1.8-installer.exe"

;;; The name and version.
!define PRODUCT_NAME "Our Personal Space"
!define PRODUCT_VERSION "1.8"

;;; Uncomment this if you want to use 3 lines for the game name. 
;; !define MUI_WELCOMEPAGE_TITLE_3LINES
;; !define MUI_FINISHPAGE_TITLE_3LINES


;;; The following settings are only shown to the user in Add/Remove programs
;;; but you'll still want to use them.

!define PRODUCT_WEB_SITE "http://metasepia.icecavern.net"
!define PRODUCT_PUBLISHER "Metasepia Games"

;;; Ignore this next block of stuff. It's mostly boilerplate.
!include "MUI.nsh"
!define MUI_ABORTWARNING

;;; Change this to change the compression scheme.
SetCompressor lzma

;;; You can change these to customize the bitmaps and icons used for
;;; your installer and uninstaller. Bitmaps should be 150x57.

; !define MUI_HEADERIMAGE
; !define MUI_HEADERIMAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Header\nsis.bmp"
; !define MUI_HEADERIMAGE_UNBITMAP "${NSISDIR}\Contrib\Graphics\Header\nsis.bmp"
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"


;;; This is the sequencing of the pages that does the actual installation.
;;; you can comment pages out, if you want to.

; Welcome page
!insertmacro MUI_PAGE_WELCOME

; License page
!insertmacro MUI_PAGE_LICENSE "LICENSE.txt"

; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\README.txt"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH


;;; Okay, that's it for the commentary. You're on your own from here...
;;; but you probably won't need to touch anything below this point.

; Various other defines.
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

; Reserve files
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS

; Language files
!insertmacro MUI_LANGUAGE "English"

;!insertmacro MUI_RESERVEFILE_LANGDLL

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "..\${INSTALLER_EXE}"
InstallDir "$PROGRAMFILES\${PRODUCT_NAME}"

Section "!${PRODUCT_NAME}" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer

  File /r /x *.pyw /x installer.nsi /x persistent *.*
  CreateDirectory "$SMPROGRAMS\${PRODUCT_NAME}"
  CreateShortCut "$SMPROGRAMS\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk" "$INSTDIR\${EXE}"
  CreateShortCut "$DESKTOP\${PRODUCT_NAME}.lnk" "$INSTDIR\${EXE}"
SectionEnd

Section -AdditionalIcons
  CreateShortCut "$SMPROGRAMS\${PRODUCT_NAME}\Uninstall.lnk" "$INSTDIR\uninst.exe"
  CreateShortCut "$SMPROGRAMS\${PRODUCT_NAME}\README.lnk" "$INSTDIR\README.txt"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\${EXE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

Section Uninstall

  Delete "$SMPROGRAMS\${PRODUCT_NAME}\README.lnk"
  Delete "$SMPROGRAMS\${PRODUCT_NAME}\Uninstall.lnk"
  Delete "$DESKTOP\${PRODUCT_NAME}.lnk"
  Delete "$SMPROGRAMS\${PRODUCT_NAME}\${PRODUCT_NAME}.lnk"

  RMDir "$SMPROGRAMS\${PRODUCT_NAME}"
  RMDir /r "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  SetAutoClose true
SectionEnd
