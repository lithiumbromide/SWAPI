---
title: "GetFocus Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "GetFocus"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~GetFocus.html"
---

# GetFocus Method (IPropertyManagerPage2)

Gets the ID of the control that has focus on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFocus() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim value As System.Integer

value = instance.GetFocus()
```

### C#

```csharp
System.int GetFocus()
```

### C++/CLI

```cpp
System.int GetFocus();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

User-defined ID of the control that has focus

## VBA Syntax

See [PropertyManagerPage2::GetFocus](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~GetFocus.html).

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[IPropertyManagerPage2::SetFocus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetFocus.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
