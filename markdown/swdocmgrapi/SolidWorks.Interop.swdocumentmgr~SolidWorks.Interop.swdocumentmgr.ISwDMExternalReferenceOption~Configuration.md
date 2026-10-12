---
title: "Configuration Property (ISwDMExternalReferenceOption)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMExternalReferenceOption"
member: "Configuration"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~Configuration.html"
---

# Configuration Property (ISwDMExternalReferenceOption)

Gets and sets the configuration from which to retrieve the information about the document's external references.

## Syntax

### Visual Basic (Declaration)

```vb
Property Configuration As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMExternalReferenceOption
Dim value As System.String

instance.Configuration = value

value = instance.Configuration
```

### C#

```csharp
System.string Configuration {get; set;}
```

### C++/CLI

```cpp
property System.String^ Configuration {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the configuration

## VBA Syntax

See [SwDMExternalReferenceOption::Configuration](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMExternalReferenceOption~Configuration.html).

## Examples

[Get External References (C#)](Get_External_References_Example_CSharp.htm)
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)

## See Also

[ISwDMExternalReferenceOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.html)
[ISwDMExternalReferenceOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption_members.html)
[ISwDMDocument15::GetExternalFeatureReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.html)

## Availability

SOLIDWORKS Document Manager API 2011 SP0
