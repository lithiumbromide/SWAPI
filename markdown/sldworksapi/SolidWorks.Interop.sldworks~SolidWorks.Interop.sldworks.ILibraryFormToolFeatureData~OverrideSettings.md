---
title: "OverrideSettings Property (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "OverrideSettings"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideSettings.html"
---

# OverrideSettings Property (ILibraryFormToolFeatureData)

Gets whether the document settings are overridden when displaying this forming tool in its flat pattern.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property OverrideSettings As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim value As System.Boolean

value = instance.OverrideSettings
```

### C#

```csharp
System.bool OverrideSettings {get;}
```

### C++/CLI

```cpp
property System.bool OverrideSettings {
   System.bool get();
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to override document settings, false to not

## VBA Syntax

See

[LibraryFormToolFeatureData::OverrideSettings](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~OverrideSettings.html)

.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

[ILibraryFormToolFeatureData::OverrideDocumentSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideDocumentSettings.html)

[ILibraryFormToolFeatureData::ShowCenter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowCenter.html)

[ILibraryFormToolFeatureData::ShowProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowProfile.html)

[ILibraryFormToolFeatureData::ShowPunch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowPunch.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
