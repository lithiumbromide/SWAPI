---
title: "SetGroupVisible Method (IPropertyManagerPage)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage"
member: "SetGroupVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage~SetGroupVisible.html"
---

# SetGroupVisible Method (IPropertyManagerPage)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetGroupVisible( _
   ByVal GroupID As System.Integer, _
   ByVal Visible As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage
Dim GroupID As System.Integer
Dim Visible As System.Boolean
Dim value As System.Integer

value = instance.SetGroupVisible(GroupID, Visible)
```

### C#

```csharp
System.int SetGroupVisible(
   System.int GroupID,
   System.bool Visible
)
```

### C++/CLI

```cpp
System.int SetGroupVisible(
   System.int GroupID,
   System.bool Visible
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupID`:
- `Visible`:

## VBA Syntax

See [PropertyManagerPage::SetGroupVisible](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage~SetGroupVisible.html).

## See Also

[IPropertyManagerPage Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage.html)
[IPropertyManagerPage Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage_members.html)
