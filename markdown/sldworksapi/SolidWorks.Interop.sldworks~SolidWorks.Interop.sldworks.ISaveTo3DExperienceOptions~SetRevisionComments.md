---
title: "SetRevisionComments Method (ISaveTo3DExperienceOptions)"
project: "SOLIDWORKS API Help"
interface: "ISaveTo3DExperienceOptions"
member: "SetRevisionComments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions~SetRevisionComments.html"
---

# SetRevisionComments Method (ISaveTo3DExperienceOptions)

Sets the specified revision comments when saving a document in [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRevisionComments( _
   ByVal RevisionComments As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISaveTo3DExperienceOptions
Dim RevisionComments As System.String
Dim value As System.Boolean

value = instance.SetRevisionComments(RevisionComments)
```

### C#

```csharp
System.bool SetRevisionComments(
   System.string RevisionComments
)
```

### C++/CLI

```cpp
System.bool SetRevisionComments(
   System.String^ RevisionComments
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RevisionComments`: Save comments

### Return Value

True if the document saved successfully, false if not

## VBA Syntax

See [SaveTo3DExperienceOptions::SetRevisionComments](ms-its:sldworksapivb6.chm::/sldworks~SaveTo3DExperienceOptions~SetRevisionComments.html).

## Examples

See the [IPLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.html) examples.

## See Also

[ISaveTo3DExperienceOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions.html)
[ISaveTo3DExperienceOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions_members.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1
