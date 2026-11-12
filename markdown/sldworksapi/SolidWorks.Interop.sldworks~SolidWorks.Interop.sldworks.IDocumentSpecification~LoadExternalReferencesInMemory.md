---
title: "LoadExternalReferencesInMemory Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "LoadExternalReferencesInMemory"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadExternalReferencesInMemory.html"
---

# LoadExternalReferencesInMemory Property (IDocumentSpecification)

Gets or sets whether to load external references in memory when opening a document.

## Syntax

### Visual Basic (Declaration)

```vb
Property LoadExternalReferencesInMemory As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.LoadExternalReferencesInMemory = value

value = instance.LoadExternalReferencesInMemory
```

### C#

```csharp
System.bool LoadExternalReferencesInMemory {get; set;}
```

### C++/CLI

```cpp
property System.bool LoadExternalReferencesInMemory {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to load external references in memory, false (default) to not

## VBA Syntax

See [DocumentSpecification::LoadExternalReferencesInMemory](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~LoadExternalReferencesInMemory.html).

## Remarks

This property is:

- not valid for opening **3D**EXPERIENCE files using [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

- valid only if [swUserPreferenceIntegerValue_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.html).swLoadExternalReferences is not set to [swLoadExternalReferences_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLoadExternalReferences_e.html).swLoadExternalReferences_None.

Note: The **System Options > External References > Load documents in memory only** user preference and [swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swExtRefLoadRefDocsInMemory are ignored when opening documents through the API because this method and [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html) ([swOpenDocOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swOpenDocOptions_e.html).swOpenDocOptions_LoadExternalReferencesInMemory) have sole control of reference loading.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
