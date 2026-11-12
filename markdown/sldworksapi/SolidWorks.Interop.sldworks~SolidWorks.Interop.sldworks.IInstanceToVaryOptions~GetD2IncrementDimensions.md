---
title: "GetD2IncrementDimensions Method (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "GetD2IncrementDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetD2IncrementDimensions.html"
---

# GetD2IncrementDimensions Method (IInstanceToVaryOptions)

Gets the dimensions to increment in Direction 2.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetD2IncrementDimensions( _
   ByRef IncrementDimensions As System.Object, _
   ByRef IncrementDimValues As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IInstanceToVaryOptions
Dim IncrementDimensions As System.Object
Dim IncrementDimValues As System.Object

instance.GetD2IncrementDimensions(IncrementDimensions, IncrementDimValues)
```

### C#

```csharp
void GetD2IncrementDimensions(
   out System.object IncrementDimensions,
   out System.object IncrementDimValues
)
```

### C++/CLI

```cpp
void GetD2IncrementDimensions(
   [Out] System.Object^ IncrementDimensions,
   [Out] System.Object^ IncrementDimValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncrementDimensions`: Array of dimensions to increment
- `IncrementDimValues`: Array of dimension increments in Direction 2

## VBA Syntax

See [InstanceToVaryOptions::GetD2IncrementDimensions](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~GetD2IncrementDimensions.html).

## See Also

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html)
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
