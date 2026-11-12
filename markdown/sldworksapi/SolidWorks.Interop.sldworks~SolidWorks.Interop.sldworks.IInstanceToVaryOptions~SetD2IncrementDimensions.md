---
title: "SetD2IncrementDimensions Method (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "SetD2IncrementDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~SetD2IncrementDimensions.html"
---

# SetD2IncrementDimensions Method (IInstanceToVaryOptions)

Sets the dimensions to increment in Direction 2.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetD2IncrementDimensions( _
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

value = instance.SetD2IncrementDimensions(IncrementDimensions, IncrementDimValues)
```

### C#

```csharp
System.bool SetD2IncrementDimensions(
   System.object IncrementDimensions,
   System.object IncrementDimValues
)
```

### C++/CLI

```cpp
System.bool SetD2IncrementDimensions(
   System.Object^ IncrementDimensions,
   System.Object^ IncrementDimValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncrementDimensions`: Array of dimensions to increment
- `IncrementDimValues`: Array of dimension increments in Direction 2

### Return Value

True if the dimensions are incremented successfully, false if not

## VBA Syntax

See [InstanceToVaryOptions::SetD2IncrementDimensions](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~SetD2IncrementDimensions.html).

## See Also

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html)
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
