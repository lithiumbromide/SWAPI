---
title: "SheetMetalProcess Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "SheetMetalProcess"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~SheetMetalProcess.html"
---

# SheetMetalProcess Property (IConvertSolidFeatureData)

Gets the sheet metal process name for this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SheetMetalProcess As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.String

value = instance.SheetMetalProcess
```

### C#

```csharp
System.string SheetMetalProcess {get;}
```

### C++/CLI

```cpp
property System.String^ SheetMetalProcess {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of sheet metal process

## VBA Syntax

See [ConvertSolidFeatureData::SheetMetalProcess](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~SheetMetalProcess.html).

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
