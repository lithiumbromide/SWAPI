---
title: "AutoRepair Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "AutoRepair"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AutoRepair.html"
---

# AutoRepair Property (IDocumentSpecification)

Gets or sets whether to automatically repair non-critical custom properties errors in the file to be opened.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoRepair As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.AutoRepair = value

value = instance.AutoRepair
```

### C#

```csharp
System.bool AutoRepair {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoRepair {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically repair custom properties errors, false to not (default) (see **Remarks**)

## VBA Syntax

See [DocumentSpecification::AutoRepair](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~AutoRepair.html).

## Remarks

This property is valid only if [IDocumentSpecification::Silent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Silent.html) is set to true.

If the document to be opened has a non-critical data error, the non-critical data error may or may not be repaired, depending on how you set this property and other conditions.

If you set this property to true, and the file to open has non-critical data corruption in:

- The custom properties area, the repair proceeds, and [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html) returns the document with warning, [swFileLoadWarning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadWarning_e.html).swFileLoadWarning_AutomaticRepair.
- An area other than custom properties, the document is not repaired.

The following files are created in c**:\Users\**`user`**\AppData\Local\Temp:**

- **Repaired_`file_name.sld*`**
- **Backup of `file_name.sld*`**

If you set this property to false, and the file to open has non-critical data corruption:

- The document is not repaired.
- The document does not open.
- [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html) fails and returns null with error code, [swFileLoadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html).FileRequiresAutoRepair.

If critical data corruption exists in the file, and you set [IDocumentSpecification::CriticalDataRepair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~CriticalDataRepair.html) to true to handle critical data corruption:

- Non-critical data corruptions are ignored and not repaired.
- Repairing critical errors necessitates obliterating all non-critical data.

Use For C++ only, VARIANT_TRUE (-1) automatically repairs the file, and VARIANT_FALSE (0) does not.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
