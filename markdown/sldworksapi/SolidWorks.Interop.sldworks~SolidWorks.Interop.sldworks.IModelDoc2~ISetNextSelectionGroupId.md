---
title: "ISetNextSelectionGroupId Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ISetNextSelectionGroupId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetNextSelectionGroupId.html"
---

# ISetNextSelectionGroupId Method (IModelDoc2)

Sets the group ID for all remaining selections.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetNextSelectionGroupId( _
   ByVal ID As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ID As System.Integer

instance.ISetNextSelectionGroupId(ID)
```

### C#

```csharp
void ISetNextSelectionGroupId(
   System.int ID
)
```

### C++/CLI

```cpp
void ISetNextSelectionGroupId(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Group ID

## VBA Syntax

See [ModelDoc2::ISetNextSelectionGroupId](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ISetNextSelectionGroupId.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
