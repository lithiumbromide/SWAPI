---
title: "GetSaveBodies Method (ISaveBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISaveBodyFeatureData"
member: "GetSaveBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~GetSaveBodies.html"
---

# GetSaveBodies Method (ISaveBodyFeatureData)

Gets the save bodies in this Save Bodies feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSaveBodies( _
   ByRef Bodies As System.Object, _
   ByRef FilePaths As System.Object, _
   ByRef Flags As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISaveBodyFeatureData
Dim Bodies As System.Object
Dim FilePaths As System.Object
Dim Flags As System.Object

instance.GetSaveBodies(Bodies, FilePaths, Flags)
```

### C#

```csharp
void GetSaveBodies(
   out System.object Bodies,
   out System.object FilePaths,
   out System.object Flags
)
```

### C++/CLI

```cpp
void GetSaveBodies(
   [Out] System.Object^ Bodies,
   [Out] System.Object^ FilePaths,
   [Out] System.Object^ Flags
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bodies`: - Array of save bodies
- `FilePaths`: Array of paths and filenames for the part documents of Bodies
- `Flags`: - Array of booleans indicating whether each corresponding save body is consumed; true if removed from the original part, false if not

## VBA Syntax

See [SaveBodyFeatureData::GetSaveBodies](ms-its:sldworksapivb6.chm::/sldworks~SaveBodyFeatureData~GetSaveBodies.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html)
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.html)
[ISaveBodyFeatureData::GetSaveBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~GetSaveBodiesCount.html)
[ISaveBodyFeatureData::AddSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~AddSaveBodies.html)
[ISaveBodyFeatureData::RemoveSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~RemoveSaveBodies.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
