---
title: "SetTolerances Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "SetTolerances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetTolerances.html"
---

# SetTolerances Method (IModeler)

Obsolete. Superseded by [IModeler::GetToleranceValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~GetToleranceValue.html) and [IModeler::SetToleranceValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~SetToleranceValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTolerances( _
   ByRef ToleranceIDArray As System.Integer, _
   ByRef ToleranceValueArray As System.Double, _
   ByVal NumTol As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim ToleranceIDArray As System.Integer
Dim ToleranceValueArray As System.Double
Dim NumTol As System.Integer
Dim value As System.Boolean

value = instance.SetTolerances(ToleranceIDArray, ToleranceValueArray, NumTol)
```

### C#

```csharp
System.bool SetTolerances(
   ref System.int ToleranceIDArray,
   ref System.double ToleranceValueArray,
   System.int NumTol
)
```

### C++/CLI

```cpp
System.bool SetTolerances(
   System.int% ToleranceIDArray,
   System.double% ToleranceValueArray,
   System.int NumTol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToleranceIDArray`: Type of tolerance you want to set as defined in [swTolerances_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolerances_e.html)
- `ToleranceValueArray`: New tolerance value in meters for the specified tolerance type
- `NumTol`: Original value of the specified tolerance type

## VBA Syntax

See [Modeler::SetTolerances](ms-its:sldworksapivb6.chm::/sldworks~Modeler~SetTolerances.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
