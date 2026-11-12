---
title: "IGetTriadRotationParameters Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "IGetTriadRotationParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadRotationParameters.html"
---

# IGetTriadRotationParameters Method (IMoveFaceFeatureData)

Gets the rotation parameters for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTriadRotationParameters() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim value As System.Double

value = instance.IGetTriadRotationParameters()
```

### C#

```csharp
System.double IGetTriadRotationParameters()
```

### C++/CLI

```cpp
System.double IGetTriadRotationParameters();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of six doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The first three doubles returned are the X, Y, and Z rotation origin parameters. The remaining three doubles returned are the X, Y, and Z rotation angle parameters.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::ISetTriadRotationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadRotationParameters.html)
[IMoveFaceFeatureData::TriadRotationParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadRotationParameters.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
