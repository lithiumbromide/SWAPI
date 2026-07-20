---
title: "ShowCenter Property (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "ShowCenter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowCenter.html"
---

# ShowCenter Property (ILibraryFormToolFeatureData)

Gets whether to display the center mark where this forming tool is located in the flat pattern.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ShowCenter As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim value As System.Boolean

value = instance.ShowCenter
```

### C#

```csharp
System.bool ShowCenter {get;}
```

### C++/CLI

```cpp
property System.bool ShowCenter {
   System.bool get();
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to display the center mark where this forming tool is located in the flat pattern, false to not

## VBA Syntax

See

[LibraryFormToolFeatureData::ShowCenter](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~ShowCenter.html)

.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

[ILibraryFormToolFeatureData::OverrideDocumentSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideDocumentSettings.html)

[ILibraryFormToolFeatureData::OverrideSettings Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideSettings.html)

[ILibraryFormToolFeatureData::ShowProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowProfile.html)

[ILibraryFormToolFeatureData::ShowPunch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowPunch.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
