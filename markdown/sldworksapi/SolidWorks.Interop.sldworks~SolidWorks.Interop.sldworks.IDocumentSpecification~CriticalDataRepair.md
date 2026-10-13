---
title: "CriticalDataRepair Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "CriticalDataRepair"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~CriticalDataRepair.html"
---

# CriticalDataRepair Property (IDocumentSpecification)

Gets or sets whether to automatically repair critical data errors in the file to be opened.

## Syntax

### Visual Basic (Declaration)

```vb
Property CriticalDataRepair As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.CriticalDataRepair = value

value = instance.CriticalDataRepair
```

### C#

```csharp
System.bool CriticalDataRepair {get; set;}
```

### C++/CLI

```cpp
property System.bool CriticalDataRepair {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically repair critical data errors, false to not

## VBA Syntax

See [DocumentSpecification::CriticalDataRepair](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~CriticalDataRepair.html).

## Remarks

This property is valid only if [IDocumentSpecification::Silent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Silent.html) is set to true.

If you set this property to true, and the file to open has critical data corruption:

- Critical data repair proceeds.
- [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html) returns the document with warning, [swFileLoadWarning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadWarning_e.html).swFileLoadWarning_CriticalDataRepair.
- All non-critical data errors are ignored, because repairing critical errors obliterates all non-critical data in the file.

If set to true, this property instructs SOLIDWORKS to repair critical data by importing Parasolid bodies into a new file. The repaired file contains only Parasolid bodies.

The following files are created in c**:\Users\**`user`**\AppData\Local\Temp:**

- **Repaired_`file_name.sld*`**
- **Backup of `file_name.sld*`**

If you set this property to false, and the file to open has critical data corruption:

- The document does not open.
- ISldWorks::OpenDoc7 fails and returns null with error code, [swFileLoadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html).FileRequiresCriticalDataRepair.

Use [IDocumentSpecification::AutoRepair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AutoRepair.html) to handle non-critical data corruption of files.

For C++ only, VARIANT_TRUE (-1) automatically repairs the file, and VARIANT_FALSE (0) does not.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
