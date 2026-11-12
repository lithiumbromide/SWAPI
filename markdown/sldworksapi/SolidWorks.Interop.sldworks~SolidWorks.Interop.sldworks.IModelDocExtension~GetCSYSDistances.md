---
title: "GetCSYSDistances Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCSYSDistances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSDistances.html"
---

# GetCSYSDistances Method (IModelDocExtension)

Gets the specified distances between two selected coordinate systems.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCSYSDistances( _
   ByRef TotDistance As System.Double, _
   ByRef XDistance As System.Double, _
   ByRef YDistance As System.Double, _
   ByRef ZDistance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim TotDistance As System.Double
Dim XDistance As System.Double
Dim YDistance As System.Double
Dim ZDistance As System.Double
Dim value As System.Boolean

value = instance.GetCSYSDistances(TotDistance, XDistance, YDistance, ZDistance)
```

### C#

```csharp
System.bool GetCSYSDistances(
   out System.double TotDistance,
   out System.double XDistance,
   out System.double YDistance,
   out System.double ZDistance
)
```

### C++/CLI

```cpp
System.bool GetCSYSDistances(
   [Out] System.double TotDistance,
   [Out] System.double XDistance,
   [Out] System.double YDistance,
   [Out] System.double ZDistance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TotDistance`: Distance between origins
- `XDistance`: Distance between X axes
- `YDistance`: Distance between Y axes
- `ZDistance`: Distance between Z axes

### Return Value

True if distances successfully retrieved, false if not

## VBA Syntax

See [ModelDocExtension::GetCSYSDistances](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetCSYSDistances.html).

## Remarks

This method corresponds to the SOLIDWORKS measure tool's calculation of distance between two coordinate systems. See **SOLIDWORKS online help > Fundamentals > Measure Tool** for more information.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetCSYSEulersAngularRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSEulersAngularRotation.html)
[IModelDocExtension::GetCSYSXYZAngularRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSXYZAngularRotation.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
