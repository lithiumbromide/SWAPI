---
title: "GetD1IncrementDimensions Method (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "GetD1IncrementDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetD1IncrementDimensions.html"
---

# GetD1IncrementDimensions Method (IInstanceToVaryOptions)

Gets the dimensions to increment in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetD1IncrementDimensions( _
   ByRef IncrementDimensions As System.Object, _
   ByRef IncrementDimValues As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IInstanceToVaryOptions
Dim IncrementDimensions As System.Object
Dim IncrementDimValues As System.Object

instance.GetD1IncrementDimensions(IncrementDimensions, IncrementDimValues)
```

### C#

```csharp
void GetD1IncrementDimensions(
   out System.object IncrementDimensions,
   out System.object IncrementDimValues
)
```

### C++/CLI

```cpp
void GetD1IncrementDimensions(
   [Out] System.Object^ IncrementDimensions,
   [Out] System.Object^ IncrementDimValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncrementDimensions`: Array of dimensions to increment
- `IncrementDimValues`: Array of dimension increments in Direction 1

## VBA Syntax

See [InstanceToVaryOptions::GetD1IncrementDimensions](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~GetD1IncrementDimensions.html).

## Examples

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) examples.

## See Also

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html)
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
