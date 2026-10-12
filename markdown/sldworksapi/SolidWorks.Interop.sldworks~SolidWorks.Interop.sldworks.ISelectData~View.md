---
title: "View Property (ISelectData)"
project: "SOLIDWORKS API Help"
interface: "ISelectData"
member: "View"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~View.html"
---

# View Property (ISelectData)

Gets or sets the drawing view that contains the selected object.

## Syntax

### Visual Basic (Declaration)

```vb
Property View As View
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectData
Dim value As View

instance.View = value

value = instance.View
```

### C#

```csharp
View View {get; set;}
```

### C++/CLI

```cpp
property View^ View {
   View^ get();
   void set (    View^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[View](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) that contains the selected object

## VBA Syntax

See [SelectData::View](ms-its:sldworksapivb6.chm::/sldworks~SelectData~View.html).

## Examples

[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)
[Set Body for View (VB.NET)](Set_Body_for_View_Example_VBNET.htm)
[Set Body for View (VBA)](Set_Body_for_View_Example_VB.htm)

## See Also

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
