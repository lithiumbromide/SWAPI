---
title: "GetUserUnit Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetUserUnit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetUserUnit.html"
---

# GetUserUnit Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetUserUnit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUserUnit.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserUnit( _
   ByVal UnitType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UnitType As System.Integer
Dim value As System.Object

value = instance.GetUserUnit(UnitType)
```

### C#

```csharp
System.object GetUserUnit(
   System.int UnitType
)
```

### C++/CLI

```cpp
System.Object^ GetUserUnit(
   System.int UnitType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UnitType`:

## VBA Syntax

See [ModelDoc::GetUserUnit](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetUserUnit.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
