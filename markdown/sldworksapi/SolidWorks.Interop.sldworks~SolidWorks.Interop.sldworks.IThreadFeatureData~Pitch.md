---
title: "Pitch Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "Pitch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Pitch.html"
---

# Pitch Property (IThreadFeatureData)

Gets or sets the pitch of the thread helix of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Pitch As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Double

instance.Pitch = value

value = instance.Pitch
```

### C#

```csharp
System.double Pitch {get; set;}
```

### C++/CLI

```cpp
property System.double Pitch {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 < Pitch of the helix; default is determined by interrogating the selected configuration's profile sketch

## VBA Syntax

See [ThreadFeatureData::Pitch](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~Pitch.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

Specify either a value or an equation that starts with an equal sign (=).

This property is valid only if [IThreadFeatureData::PitchOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~PitchOverride.html) is set to true.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)
[IThreadFeatureData::MultipleStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MultipleStart.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
