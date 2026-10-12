---
title: "ConfigurationID Property (ISwDMComponent8)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent8"
member: "ConfigurationID"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent8~ConfigurationID.html"
---

# ConfigurationID Property (ISwDMComponent8)

Gets the ID of the configuration of this component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConfigurationID As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent8
Dim value As System.Integer

value = instance.ConfigurationID
```

### C#

```csharp
System.int ConfigurationID {get;}
```

### C++/CLI

```cpp
property System.int ConfigurationID {
   System.int get();
}
```

### Property Value

Configuration ID

## VBA Syntax

See [SwDMComponent8::ConfigurationID](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent8~ConfigurationID.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)

## Remarks

SOLIDWORKS does not update suppressed assembly components with changes that occur in referenced documents. For instance, if a component's configuration is renamed, the suppressed component in the assembly is not updated with the new configuration name.

To find the current configuration name of a suppressed component in an assembly, query the referenced component document for the name of the configuration whose ID matches ISwDMComponent8::ConfigurationID.

## See Also

[ISwDMComponent8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent8.html)
[ISwDMComponent8 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent8_members.html)

## Availability

SOLIDWORKS 2010 SP05, Revision Number 18.5 and SOLIDWORKS 2011 SP01, Revision Number 19.1
