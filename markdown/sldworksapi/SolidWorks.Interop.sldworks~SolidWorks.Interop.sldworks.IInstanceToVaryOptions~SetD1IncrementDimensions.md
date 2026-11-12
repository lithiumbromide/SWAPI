---
title: "SetD1IncrementDimensions Method (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "SetD1IncrementDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~SetD1IncrementDimensions.html"
---

# SetD1IncrementDimensions Method (IInstanceToVaryOptions)

Sets the dimensions to increment in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetD1IncrementDimensions( _
   ByVal IncrementDimensions As System.Object, _
   ByVal IncrementDimValues As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInstanceToVaryOptions
Dim IncrementDimensions As System.Object
Dim IncrementDimValues As System.Object
Dim value As System.Boolean

value = instance.SetD1IncrementDimensions(IncrementDimensions, IncrementDimValues)
```

### C#

```csharp
System.bool SetD1IncrementDimensions(
   System.object IncrementDimensions,
   System.object IncrementDimValues
)
```

### C++/CLI

```cpp
System.bool SetD1IncrementDimensions(
   System.Object^ IncrementDimensions,
   System.Object^ IncrementDimValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncrementDimensions`: Array of dimensions to increment
- `IncrementDimValues`: Array of dimension increments in Direction 1

### Return Value

True if the dimensions are incremented successfully, false if not

## VBA Syntax

See [InstanceToVaryOptions::SetD1IncrementDimensions](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~SetD1IncrementDimensions.html).

## Examples

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) examples.

## See Also

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html)
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
