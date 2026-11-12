---
title: "AddSaveBodies Method (ISaveBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISaveBodyFeatureData"
member: "AddSaveBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~AddSaveBodies.html"
---

# AddSaveBodies Method (ISaveBodyFeatureData)

Adds the specified bodies to the Save Bodies feature and saves them as part documents on disk.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSaveBodies( _
   ByVal Bodies As System.Object, _
   ByVal FilePaths As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISaveBodyFeatureData
Dim Bodies As System.Object
Dim FilePaths As System.Object
Dim value As System.Boolean

value = instance.AddSaveBodies(Bodies, FilePaths)
```

### C#

```csharp
System.bool AddSaveBodies(
   System.object Bodies,
   System.object FilePaths
)
```

### C++/CLI

```cpp
System.bool AddSaveBodies(
   System.Object^ Bodies,
   System.Object^ FilePaths
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bodies`: Array of bodies to add to the Save Bodies feature
- `FilePaths`: - Array of path and filenames of part documents to which to save Bodies

### Return Value

True if the bodies are added to the Save Bodies feature and saved as part documents on disk, false if not

## VBA Syntax

See [SaveBodyFeatureData::AddSaveBodies](ms-its:sldworksapivb6.chm::/sldworks~SaveBodyFeatureData~AddSaveBodies.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html)
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.html)
[ISaveBodyFeatureData::GetSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~GetSaveBodies.html)
[ISaveBodyFeatureData::RemoveSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~RemoveSaveBodies.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
