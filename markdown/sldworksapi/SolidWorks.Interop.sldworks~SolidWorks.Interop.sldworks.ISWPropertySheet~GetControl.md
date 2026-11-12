---
title: "GetControl Method (ISWPropertySheet)"
project: "SOLIDWORKS API Help"
interface: "ISWPropertySheet"
member: "GetControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~GetControl.html"
---

# GetControl Method (ISWPropertySheet)

Gets the ActiveX control on the property sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControl( _
   ByVal PageIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISWPropertySheet
Dim PageIndex As System.Integer
Dim value As System.Object

value = instance.GetControl(PageIndex)
```

### C#

```csharp
System.object GetControl(
   System.int PageIndex
)
```

### C++/CLI

```cpp
System.Object^ GetControl(
   System.int PageIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PageIndex`: Index of property sheet

### Return Value

ActiveX control

## VBA Syntax

See [SWPropertySheet::GetControl](ms-its:sldworksapivb6.chm::/sldworks~SWPropertySheet~GetControl.html).

## Remarks

Typically, you would call this method from the ISWPropertySheet [OnOKNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSWPropertySheetEvents_OnOKNotifyEventHandler.html) event handler to retrieve data from your ActiveX control.

## See Also

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.html)
[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
