---
title: "UnsetTolerances Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "UnsetTolerances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~UnsetTolerances.html"
---

# UnsetTolerances Method (IModeler)

Sets the tolerances back to system settings.

## Syntax

### Visual Basic (Declaration)

```vb
Function UnsetTolerances( _
   ByRef ToleranceIDArray As System.Integer, _
   ByVal NumTol As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim ToleranceIDArray As System.Integer
Dim NumTol As System.Integer
Dim value As System.Boolean

value = instance.UnsetTolerances(ToleranceIDArray, NumTol)
```

### C#

```csharp
System.bool UnsetTolerances(
   ref System.int ToleranceIDArray,
   System.int NumTol
)
```

### C++/CLI

```cpp
System.bool UnsetTolerances(
   System.int% ToleranceIDArray,
   System.int NumTol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToleranceIDArray`: Array specifying the tolerances to reset as defined in [swTolerances_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolerances_e.html)
- `NumTol`: Number of tolerance types you are resetting; this value should correspond to the number of elements in the ToleranceIDArray array

### Return Value

True if the tolerances is reset successfully, false if n

## VBA Syntax

See [Modeler::UnsetTolerances](ms-its:sldworksapivb6.chm::/sldworks~Modeler~UnsetTolerances.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::GetToleranceValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetToleranceValue.html)
[IModeler::SetToleranceValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.html)
