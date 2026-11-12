---
title: "ISetTriadRotationParameters Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "ISetTriadRotationParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadRotationParameters.html"
---

# ISetTriadRotationParameters Method (IMoveFaceFeatureData)

Sets the rotation parameters for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetTriadRotationParameters( _
   ByRef RotationParameters As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim RotationParameters As System.Double

instance.ISetTriadRotationParameters(RotationParameters)
```

### C#

```csharp
void ISetTriadRotationParameters(
   ref System.double RotationParameters
)
```

### C++/CLI

```cpp
void ISetTriadRotationParameters(
   System.double% RotationParameters
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RotationParameters`: - in-process, unmanaged C++: pointer to an array of six doubles for the rotation parameters (see **Remarks**)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

The first three doubles are the X, Y, and Z rotation origin parameters. The remaining three doubles are the X, Y, and Z rotation angle parameters.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::IGetTriadRotationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadRotationParameters.html)
[IMoveFaceFeatureData::TriadRotationParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadRotationParameters.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
