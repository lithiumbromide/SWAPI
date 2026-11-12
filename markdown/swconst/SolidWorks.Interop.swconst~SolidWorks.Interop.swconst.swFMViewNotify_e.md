---
title: "swFMViewNotify_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFMViewNotify_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFMViewNotify_e.html"
---

# swFMViewNotify_e Enumeration

FeatureManager design tree notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFMViewNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFMViewNotify_e
```

### C#

```csharp
public enum swFMViewNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFMViewNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFMViewActivateNotify | 1 = ActivateNotify |
| swFMViewDeactivateNotify | 2 = DeactivateNotify |
| swFMViewDestroyNotify | 3 = DestroyNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports FeatureManager design tree events (e.g., FeatMgrView.h), include:

```vb
DECLARE_REGISTRY_RESOURCEID(IDR_FeatMgrView)
BEGIN_SINK_MAP(CFeatMgrView)
SINK_ENTRY_EX(ID_FEATMGRVIEW_EVENTS, DIID_DFeatMgrViewEvents, swFMViewDestroyNotify , DestroyNotify)
SINK_ENTRY_EX(ID_FEATMGRVIEW_EVENTS, DIID_DFeatMgrViewEvents, swFMViewActivateNotify, ActivateNotify)
SINK_ENTRY_EX(ID_FEATMGRVIEW_EVENTS, DIID_DFeatMgrViewEvents, swFMViewDeactivateNotify , DeActivateNotify)
END_SINK_MAP()
```

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/Overview/events.htm) for [IFeatMgrView](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView.html) events.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
