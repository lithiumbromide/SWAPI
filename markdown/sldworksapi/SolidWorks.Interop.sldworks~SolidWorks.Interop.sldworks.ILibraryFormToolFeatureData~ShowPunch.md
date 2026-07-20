---
title: "ShowPunch Property (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "ShowPunch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowPunch.html"
---

# ShowPunch Property (ILibraryFormToolFeatureData)

Gets whether to display the cut of this forming tool when the part is flattened.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ShowPunch As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim value As System.Boolean

value = instance.ShowPunch
```

### C#

```csharp
System.bool ShowPunch {get;}
```

### C++/CLI

```cpp
property System.bool ShowPunch {
   System.bool get();
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to display the cut of this forming tool when the part is flattened, false to not

## VBA Syntax

See

[LibraryFormToolFeatureData::ShowPunch](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~ShowPunch.html)

.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

[ILibraryFormToolFeatureData::OverrideDocumentSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideDocumentSettings.html)

[ILibraryFormToolFeatureData::OverrideSettings Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideSettings.html)

[ILibraryFormToolFeatureData::ShowCenter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowCenter.html)

[ILibraryFormToolFeatureData::ShowProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowProfile.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
