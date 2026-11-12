---
title: "ICopyWizardHole Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICopyWizardHole"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICopyWizardHole.html"
---

# ICopyWizardHole Method (IModeler)

Copies hole data from the source hole to the destination hole.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICopyWizardHole( _
   ByVal SourceHole As Feature, _
   ByVal DestinationHole As Feature, _
   ByVal RebuildOwner As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim SourceHole As Feature
Dim DestinationHole As Feature
Dim RebuildOwner As System.Boolean
Dim value As System.Integer

value = instance.ICopyWizardHole(SourceHole, DestinationHole, RebuildOwner)
```

### C#

```csharp
System.int ICopyWizardHole(
   Feature SourceHole,
   Feature DestinationHole,
   System.bool RebuildOwner
)
```

### C++/CLI

```cpp
System.int ICopyWizardHole(
   Feature^ SourceHole,
   Feature^ DestinationHole,
   System.bool RebuildOwner
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SourceHole`: [Source hole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- `DestinationHole`: [Destination hole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- `RebuildOwner`: True rebuilds the model, false does not

### Return Value

0 if the call generated an error; 1 if the call did not generate an error

## VBA Syntax

See [Modeler::ICopyWizardHole](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICopyWizardHole.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CopyWizardHole Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CopyWizardHole.html)
[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
