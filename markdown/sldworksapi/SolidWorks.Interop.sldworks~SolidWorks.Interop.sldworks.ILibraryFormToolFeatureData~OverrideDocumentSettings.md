---
title: "OverrideDocumentSettings Method (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "OverrideDocumentSettings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideDocumentSettings.html"
---

# OverrideDocumentSettings Method (ILibraryFormToolFeatureData)

Specifies the flat pattern visibility options for this forming tool feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OverrideDocumentSettings( _
   ByVal OverrideSettings As System.Boolean, _
   ByVal ShowPunch As System.Boolean, _
   ByVal ShowProfile As System.Boolean, _
   ByVal ShowCenter As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim OverrideSettings As System.Boolean
Dim ShowPunch As System.Boolean
Dim ShowProfile As System.Boolean
Dim ShowCenter As System.Boolean

instance.OverrideDocumentSettings(OverrideSettings, ShowPunch, ShowProfile, ShowCenter)
```

### C#

```csharp
void OverrideDocumentSettings(
   System.bool OverrideSettings,
   System.bool ShowPunch,
   System.bool ShowProfile,
   System.bool ShowCenter
)
```

### C++/CLI

```cpp
void OverrideDocumentSettings(
   System.bool OverrideSettings,
   System.bool ShowPunch,
   System.bool ShowProfile,
   System.bool ShowCenter
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `OverrideSettings`: True to override the options set in

Tools > Options > Document Properties > Sheet Metal

, false to not (see

Remarks

)
- `ShowPunch`: True to display the cut of this forming tool when the part is flattened, false to not (see

Remarks

)
- `ShowProfile`: True to display the placement sketch of this forming tool when the part is flattened, false to not (see

Remarks

)
- `ShowCenter`: True to display the center mark where this forming tool is located in the flat pattern, false to not (see

Remarks

)

## VBA Syntax

See

[LibraryFormToolFeatureData::OverrideDocumentSettings](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~OverrideDocumentSettings.html)

.

## Examples

See the

[ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

examples.

## Remarks

ShowPunch, ShowProfile, and ShowCenter are valid only if OverrideSettings is set to true.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

[ILibraryFormToolFeatureData::OverrideSettings Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideSettings.html)

[ILibraryFormToolFeatureData::ShowCenter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowCenter.html)

[ILibraryFormToolFeatureData::ShowProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowProfile.html)

[ILibraryFormToolFeatureData::ShowPunch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowPunch.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
