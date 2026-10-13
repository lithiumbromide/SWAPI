---
title: "ICustomBendAllowance Interface"
project: "SOLIDWORKS API Help"
interface: "ICustomBendAllowance"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html"
---

# ICustomBendAllowance Interface

Allows access to the custom bend allowance of a feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICustomBendAllowance
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomBendAllowance
```

### C#

```csharp
public interface ICustomBendAllowance
```

### C++/CLI

```cpp
public interface class ICustomBendAllowance
```

## VBA Syntax

See [CustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~CustomBendAllowance.html).

## Examples

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)

## Remarks

In your application, the [ICustomBendAllowance::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type.html) must always be set last, after the other properties of this interface have been set. The property last set automically overrides any previously set ICustomBendAllowance::Type.

For example:

cba.**Type** = swBendAllowanceTypes_e.swBendAllowanceDeduction '***set first, so will not hold***

'***RESET THE VALUES***

cba.**KFactor** = 0.08

cba.**BendDeduction** = 0.1

cba.**BendAllowance** = 0.11

cba.**BendTableFile** = "E:\AAA Projects\sw2025\QA\SP02\Convert To Sheetmetal FUN156195\1-Staal.xls"

cba.**BendCalculationTableFile** = "E:\AAA Projects\sw2025\QA\SP02\Convert To Sheetmetal FUN156195\1-Staal.xls"

**cba.Type = swBendAllowanceTypes_e.swBendAllowanceDirect '***set last, so holds******

**The above code sets the ICustomBendAllowance::Type as swBendAllowanceTypes_e.swBendAllowanceDirect.**

Another example:

cba.**Type** = swBendAllowanceTypes_e.swBendAllowanceDeduction '***set first, so will not hold***

'***RESET THE VALUES***

cba.**KFactor** = 0.08

cba.**BendDeduction** = 0.1

cba.**BendAllowance** = 0.11

cba.**BendTableFile** = "E:\AAA Projects\sw2025\QA\SP02\Convert To Sheetmetal FUN156195\1-Staal.xls"

cba.**BendCalculationTableFile** = "E:\AAA Projects\sw2025\QA\SP02\Convert To Sheetmetal FUN156195\1-Staal.xls"

**‘cba.**Type **= swBendAllowanceTypes_e.swBendAllowanceDirect '***set last would hold**** BUT COMMENTED OUT**

**The above code sets the ICustomBendAllowance::Type as swBendAllowanceTypes_e.swBendAllowanceBendCalculationTable, because the last property set was BendCalculationTableFile.**

The last ICustomBendAllowance property that is set automatically re-sets the type of bend allowance. You can always explicitly specify the [ICustomBendAllowance::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type.html), but you must set it after all other properties of this interface have been set.

## Accessors

[IBaseFlangeFeatureData::GetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetCustomBendAllowance.html)

[IBendsFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.html)

[IEdgeFlangeFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdgeFlangeFeatureData~GetCustomBendAllowance.html)

[IFeatureManager::CreateCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateCustomBendAllowance.html)

[IHemFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHemFeatureData~GetCustomBendAllowance.html)

[IJogFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJogFeatureData~GetCustomBendAllowance.html)

[IMiterFlangeFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData.html)

[IOneBendFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~GetCustomBendAllowance.html)

[ISheetMetalFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData~GetCustomBendAllowance.html)

[ISketchedBendFeatureData::GetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~GetCustomBendAllowance.html)

[ISweptFlangeFeatureData::GetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetCustomBendAllowance.html)

## Access Diagram

[CustomBendAllowance](SWObjectModel.pdf#CustomBendAllowance)

## See Also

[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
