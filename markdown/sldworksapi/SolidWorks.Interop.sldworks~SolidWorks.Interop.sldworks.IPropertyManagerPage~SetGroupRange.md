---
title: "SetGroupRange Method (IPropertyManagerPage)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage"
member: "SetGroupRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage~SetGroupRange.html"
---

# SetGroupRange Method (IPropertyManagerPage)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetGroupRange( _
   ByVal FirstGroupId As System.Integer, _
   ByVal FirstCheckId As System.Integer, _
   ByVal GroupCount As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage
Dim FirstGroupId As System.Integer
Dim FirstCheckId As System.Integer
Dim GroupCount As System.Integer
Dim value As System.Integer

value = instance.SetGroupRange(FirstGroupId, FirstCheckId, GroupCount)
```

### C#

```csharp
System.int SetGroupRange(
   System.int FirstGroupId,
   System.int FirstCheckId,
   System.int GroupCount
)
```

### C++/CLI

```cpp
System.int SetGroupRange(
   System.int FirstGroupId,
   System.int FirstCheckId,
   System.int GroupCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstGroupId`:
- `FirstCheckId`:
- `GroupCount`:

## VBA Syntax

See [PropertyManagerPage::SetGroupRange](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage~SetGroupRange.html).

## See Also

[IPropertyManagerPage Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage.html)
[IPropertyManagerPage Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage_members.html)
