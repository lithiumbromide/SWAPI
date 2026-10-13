---
title: "FileName Property (ISaveTo3DExperienceOptions)"
project: "SOLIDWORKS API Help"
interface: "ISaveTo3DExperienceOptions"
member: "FileName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions~FileName.html"
---

# FileName Property (ISaveTo3DExperienceOptions)

Gets or sets the specified file name when saving a document in [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Property FileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISaveTo3DExperienceOptions
Dim value As System.String

instance.FileName = value

value = instance.FileName
```

### C#

```csharp
System.string FileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

File name

## VBA Syntax

See [SaveTo3DExperienceOptions::FileName](ms-its:sldworksapivb6.chm::/sldworks~SaveTo3DExperienceOptions~FileName.html).

## Examples

See the [IPLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.html) examples.

## See Also

[ISaveTo3DExperienceOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions.html)
[ISaveTo3DExperienceOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions_members.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1
