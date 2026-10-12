---
title: "swPropertySheetNotify_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropertySheetNotify_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertySheetNotify_e.html"
---

# swPropertySheetNotify_e Enumeration

Property sheet notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropertySheetNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropertySheetNotify_e
```

### C#

```csharp
public enum swPropertySheetNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropertySheetNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropertySheetCreateControlNotify | 5 = CreateControlNotify |
| swPropertySheetDestroyNotify | 1 = DestroyNotify |
| swPropertySheetHelpNotify | 2 = HelpNotify |
| swPropertySheetOnCancelNotify | 4 = OnCancelNotify |
| swPropertySheetOnOKNotify | 3 = OnOKNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports property sheet events ( e.g., SwPropertySheet.h), include:

```vb
BEGIN_SINK_MAP(CSwPropertySheet)
SINK_ENTRY_EX(ID_SWPROPERTYSHEET_EVENTS, DIID_DSwPropertySheetEvents, swPropertySheetCreateControlNotify, CreateControlNotify)
SINK_ENTRY_EX(ID_SWPROPERTYSHEET_EVENTS, DIID_DSwPropertySheetEvents, swPropertySheetDestroyNotify, DestroyNotify)
END_SINK_MAP()
If developing a C++ application, use these enumerators to register for notifications for ISWPropertySheet events.
```

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
