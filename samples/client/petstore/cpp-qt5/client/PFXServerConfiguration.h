/**
 * OpenAPI Petstore
 * This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * Representing a Server configuration.
 */
#ifndef PFX_SERVERVCONFIGURATION_H
#define PFX_SERVERVCONFIGURATION_H
#include <QString>
#include <QMap>
#include <QRegularExpression>
#include <stdexcept>
#include "PFXServerVariable.h"

namespace test_namespace {

class PFXServerConfiguration {
public:
    /**
     * @param URL A URL to the target host.
     * @param description A description of the host designated by the URL.
     * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
     */
    PFXServerConfiguration(const QString& URL, const QString& description, const QMap<QString, PFXServerVariable>& variables)
    : _description(description),
      _variables(variables),
      _URL(URL){}
    PFXServerConfiguration(){}
    ~PFXServerConfiguration(){}

    /**
     * Format URL template using given variables.
     *
     * @param variables A map between a variable name and its value.
     * @return Formatted URL.
     */
    QString URL() {
        QString url = _URL;
        if(!_variables.empty()){
            // go through variables and replace placeholders
            for (auto const& v : _variables.keys()) {
                QString name = v;
                PFXServerVariable serverVariable = _variables.value(v);
                QString value = serverVariable._defaultValue;

                if (!serverVariable._enumValues.empty() && !serverVariable._enumValues.contains(value)) {
                    throw std::runtime_error(QString("The variable " + name + " in the server URL has invalid value " + value + ".").toUtf8());
                }
                QRegularExpression regex(QString("\\{" + name + "\\}"));
                url = url.replace(regex, value);

            }
            return url;
        }
        return url;
    }

    int setDefaultValue(const QString& variable,const QString& value){
      if(_variables.contains(variable))
        return _variables[variable].setDefaultValue(value);
      return -1;
    }

    QString _description;
    QMap<QString, PFXServerVariable> _variables;
    QString _URL;

};

} // namespace test_namespace

#endif // PFX_SERVERVCONFIGURATION_H
