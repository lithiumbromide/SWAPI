---
title: "swAppNotify_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAppNotify_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppNotify_e.html"
---

# swAppNotify_e Enumeration

Application notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAppNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAppNotify_e
```

### C#

```csharp
public enum swAppNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAppNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAppActiveDocChangeNotify | 4 = ActiveDocChangeNotify |
| swAppActiveModelDocChangeNotify | 5 = ActiveModelDocChangeNotify |
| swAppBackgroundProcessingEndNotify | 34 = BackgroundProcessingEndNotify |
| swAppBackgroundProcessingStartNotify | 33 = BackgroundProcessingStartNotify |
| swAppBegin3DInterconnectTranslationNotify | 37 = Begin3DInterconnectTranslationNotify |
| swAppBeginRecordNotify | 24 = Not used. |
| swAppBeginTranslationNotify | 16 = BeginTranslationNotify |
| swAppCommandCloseNotify | 29 = CommandCloseNotify |
| swAppCommandOpenPreNotify | 31 = CommandOpenPreNotify |
| swAppDestroyNotify | 3 = DestroyNotify |
| swAppDisplayPaneActivationNotify | 45 = DisplayPaneActivationNotify |
| swAppDocumentConversionNotify | 9 = DocumentConversionNotify |
| swAppDocumentLoadNotify | 27 = Obsolete |
| swAppDocumentLoadNotify2 | 28 = DocumentLoadNotify2 |
| swAppEnd3DInterconnectTranslationNotify | 38 = End3DInterconnectTranslationNotify |
| swAppEndRecordNotify | 25 = Not used. |
| swAppEndTranslationNotify | 16 = EndTranslationNotify |
| swAppFileCloseNotify | 32 = FileCloseNotify |
| swAppFileNewNotify | 2 = Obsolete |
| swAppFileNewNotify2 | 12 = FileNewNotify2 NOTE: Because it is possible to have a NULL active document when an add-in is notified using swAppFileOpenNotify2, use ISldWorks::IGetOpenDocumentByName2 instead of ISldWorks::IActiveDoc2 . |
| swAppFileNewPreNotify | 26 = FileNewPreNotify |
| swAppFileOpenNotify | 1 = Obsolete |
| swAppFileOpenNotify2 | 13 = FileOpenNotify2 |
| swAppFileOpenPostNotify | 22 = FileOpenPostNotify |
| swAppFileOpenPreNotify | 21 = FileOpenPreNotify |
| swAppInterfaceBrightnessThemeChangeNotify | 35 = InterfaceBrightnessThemeChangeNotify |
| swAppJournalWriteNotify | 27 = Not used. |
| swAppLightPMCreateNotify | Not used. |
| swAppLightSheetCreateNotify | 18 = LightSheetCreateNotify |
| swAppLightweightComponentOpenNotify | 10 = Not used. |
| swAppNonNativeFileOpenNotify | 7 = NonNativeFileOpenNotify |
| swAppOn3DExperienceStateChangeNotify | 46 = On3DExperienceStateChangeNotify |
| swAppOnIdleNotify | 20 = OnIdleNotify |
| swAppPromptForFilenameNotify | 15 = PromptForFilenameNotify |
| swAppPromptForMultipleFilenamesNotify | 30 = PromptForMultipleFileNamesNotify |
| swAppPropertySheetCreateNotify | 6 = PropertySheetCreateNotify |
| swAppReferencedFilePreNotify | 23 = ReferencedFilePreNotify |
| swAppReferencedFilePreNotify2 | 36 = ReferencedFilePreNotify2 |
| swAppReferenceNotFoundNotify | 14 = ReferenceNotFoundNotify |
| swAppStandardsDatabaseChangeNotify | 19 = Not used. |
| swAppTaskPaneCollapseNotify | 44 = TaskPaneCollapseNotify |
| swAppTaskPaneExpandNotify | 43 = TaskPaneExpandNotify |
| swAppTaskPaneHideNotify | 41 = TaskPaneHideNotify |
| swAppTaskPanePinnedNotify | 39 = TaskPanePinnedNotify |
| swAppTaskPaneShowNotify | 42 = TaskPaneShowNotify |
| swAppTaskPaneUnpinnedNotify | 40 = TaskPaneUnpinnedNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports SOLIDWORKS events ( <ATL_object_name>.h), include:

BEGIN_SINK_MAP(C<A TL_object_name >)

SINK_ENTRY_EX(ID_SLDWORKS_EVENTS, DIID_DSldWorksEvents, swAppDocumentLoadNotify, DocumentLoadNotify)

SINK_ENTRY_EX(ID_SLDWORKS_EVENTS, DIID_DSldWorksEvents, swAppFileNewNotify2, FileNewNotify2)

SINK_ENTRY_EX(ID_SLDWORKS_EVENTS, DIID_DSldWorksEvents, swAppActiveDocChangeNotify, ActiveDocChangeNotify)

SINK_ENTRY_EX(ID_SLDWORKS_EVENTS, DIID_DSldWorksEvents, swAppActiveModelDocChangeNotify, ActiveModelDocChangeNotify)

END_SINK_MAP()

If developing a C++ application, use the enumerators to[register for notifications](sldworksapiprogguide.chm::/overview/events.htm)for the[ISldWorks](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks.html)events.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
