---
title: "SetGroupExpanded Method (IPropertyManagerPage)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage"
member: "SetGroupExpanded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage~SetGroupExpanded.html"
---

# SetGroupExpanded Method (IPropertyManagerPage)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetGroupExpanded( _
   ByVal GroupID As System.Integer, _
   ByVal Expanded As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage
Dim GroupID As System.Integer
Dim Expanded As System.Boolean
Dim value As System.Integer

value = instance.SetGroupExpanded(GroupID, Expanded)
```

### C#

```csharp
System.int SetGroupExpanded(
   System.int GroupID,
   System.bool Expanded
)
```

### C++/CLI

```cpp
System.int SetGroupExpanded(
   System.int GroupID,
   System.bool Expanded
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupID`:
- `Expanded`:

## VBA Syntax

See [PropertyManagerPage::SetGroupExpanded](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage~SetGroupExpanded.html).

## See Also

[IPropertyManagerPage Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage.html)
[IPropertyManagerPage Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage_members.html)
