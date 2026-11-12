---
title: "CopyWizardHole Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CopyWizardHole"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CopyWizardHole.html"
---

# CopyWizardHole Method (IModeler)

Copies hole data from the source hole to the destination hole.

## Syntax

### Visual Basic (Declaration)

```vb
Function CopyWizardHole( _
   ByVal SourceHole As System.Object, _
   ByVal DestinationHole As System.Object, _
   ByVal RebuildOwner As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim SourceHole As System.Object
Dim DestinationHole As System.Object
Dim RebuildOwner As System.Boolean
Dim value As System.Integer

value = instance.CopyWizardHole(SourceHole, DestinationHole, RebuildOwner)
```

### C#

```csharp
System.int CopyWizardHole(
   System.object SourceHole,
   System.object DestinationHole,
   System.bool RebuildOwner
)
```

### C++/CLI

```cpp
System.int CopyWizardHole(
   System.Object^ SourceHole,
   System.Object^ DestinationHole,
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

See [Modeler::CopyWizardHole](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CopyWizardHole.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ICopyWizardHole Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICopyWizardHole.html)
[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
