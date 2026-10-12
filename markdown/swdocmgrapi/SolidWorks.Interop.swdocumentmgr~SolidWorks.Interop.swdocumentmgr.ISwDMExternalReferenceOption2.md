---
title: "ISwDMExternalReferenceOption2 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMExternalReferenceOption2"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2.html"
---

# ISwDMExternalReferenceOption2 Interface

Allows you to access information about external references from a document.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMExternalReferenceOption2
   Inherits ISwDMExternalReferenceOption
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMExternalReferenceOption2
```

### C#

```csharp
public interface ISwDMExternalReferenceOption2 : ISwDMExternalReferenceOption
```

### C++/CLI

```cpp
public interface class ISwDMExternalReferenceOption2 : public ISwDMExternalReferenceOption
```

## VBA Syntax

See [SwDMExternalReferenceOption2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMExternalReferenceOption2.html).

## Examples

[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)

## Remarks

- You can access an SwDMExternalReferenceOption2 object by calling QueryInterface on an [ISwDMExternalReferenceOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMExternalReferenceOption object can be assigned to a SwDMExternalReferenceOption2 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMApplication4::GetExternalReferenceOptionObject2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication4~GetExternalReferenceOptionObject2.html)

## See Also

[ISwDMExternalReferenceOption2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMDocument18::GetExternalFeatureReferences2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument18~GetExternalFeatureReferences2.html)
