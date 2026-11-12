---
title: "CalloutString Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "CalloutString"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~CalloutString.html"
---

# CalloutString Property (IAdvancedHoleElementData)

Gets or sets the hole callout string for this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property CalloutString As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.String

instance.CalloutString = value

value = instance.CalloutString
```

### C#

```csharp
System.string CalloutString {get; set;}
```

### C++/CLI

```cpp
property System.String^ CalloutString {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hole callout string (see **Remarks**)

## VBA Syntax

See [AdvancedHoleElementData::CalloutString](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~CalloutString.html).

## Examples

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) examples.

## Remarks

This property is valid only if [IAdvancedHoleFeatureData::CustomizeCallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~CustomizeCallout.html) is set to true.

The hole callout string is formatted as follows:

<`LibraryName`-`SymbolName`> <`callout_var1`> <`callout_var2`>... <`callout_varn`>

where:

- `LibraryName` and `SymbolName` are defined in `c:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.`
- `callout_var1-n` are callout variables. Use [IModelDocExtension::GetCalloutVariableString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCalloutVariableString.html) to get the strings for hole callout variables defined in [swCalloutVariable_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariable_e.html). You can also find the hole callout variable strings by clicking **Hole Callout > Callout Variables** in the Advanced Hole PropertyManager.

**Note**: You must include the right- and left-angle brackets and the hyphens when setting the elements of this property string:

```
   "<HOLE-SPOT><MOD-DIAM> <ah-cboredia> <HOLE-DEPTH> <ah-cboredepth><ah-cboreside>"
```

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
