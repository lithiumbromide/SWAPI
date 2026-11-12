---
title: "GetSplineParamsCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSplineParamsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount.html"
---

# GetSplineParamsCount Method (ISketch)

Obsolete. Superseded by [ISketch::GetSplineParamsCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSplineParamsCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineParamsCount( _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetSplineParamsCount(Size)
```

### C#

```csharp
System.int GetSplineParamsCount(
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetSplineParamsCount(
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`:

## VBA Syntax

See [Sketch::GetSplineParamsCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSplineParamsCount.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
