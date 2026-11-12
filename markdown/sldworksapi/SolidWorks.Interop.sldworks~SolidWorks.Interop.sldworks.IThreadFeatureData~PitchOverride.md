---
title: "PitchOverride Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "PitchOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~PitchOverride.html"
---

# PitchOverride Property (IThreadFeatureData)

Gets or sets whether to override the pitch of the thread helix of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PitchOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.PitchOverride = value

value = instance.PitchOverride
```

### C#

```csharp
System.bool PitchOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool PitchOverride {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the pitch, false to not (default)

## VBA Syntax

See [ThreadFeatureData::PitchOverride](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~PitchOverride.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

If this property is set to true, use [IThreadFeatureData::Pitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Pitch.html) to set the pitch of the thread helix.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
