---
title: "IGetUserUnit Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetUserUnit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetUserUnit.html"
---

# IGetUserUnit Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetUserUnit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetUserUnit.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUserUnit( _
   ByVal UnitType As System.Integer _
) As UserUnit
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UnitType As System.Integer
Dim value As UserUnit

value = instance.IGetUserUnit(UnitType)
```

### C#

```csharp
UserUnit IGetUserUnit(
   System.int UnitType
)
```

### C++/CLI

```cpp
UserUnit^ IGetUserUnit(
   System.int UnitType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UnitType`:

## VBA Syntax

See [ModelDoc::IGetUserUnit](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetUserUnit.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
