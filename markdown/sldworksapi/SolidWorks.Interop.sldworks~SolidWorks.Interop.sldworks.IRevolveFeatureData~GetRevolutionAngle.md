---
title: "GetRevolutionAngle Method (IRevolveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData"
member: "GetRevolutionAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData~GetRevolutionAngle.html"
---

# GetRevolutionAngle Method (IRevolveFeatureData)

Obsolete. Superseded by [IRevolveFeatureData2::GetRevolutionAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~GetRevolutionAngle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevolutionAngle( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData
Dim Forward As System.Boolean
Dim value As System.Double

value = instance.GetRevolutionAngle(Forward)
```

### C#

```csharp
System.double GetRevolutionAngle(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.double GetRevolutionAngle(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:

## VBA Syntax

See [RevolveFeatureData::GetRevolutionAngle](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData~GetRevolutionAngle.html).

## See Also

[IRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData.html)
[IRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData_members.html)
