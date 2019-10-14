# What is scheduledledger?

scheduledledger can automatically add monthly reoccurring transaction to your [ledger](https://ledger-cli.org)-file.
It uses [rclone](https://rclone.org) by default to sync your ledgerfile to cloud storage of your choice.

# How to use scheduledledger?

scheduledledger should be setup on an always on computer. A Raspberry Pi of some kind is a great choice.

# Install

1. Setup `python3` with the following packages:
    - `schedule`
    - `pyyaml`
    - `subprocess`
2. Install `rclone` and setup your cloud storage
3. Clone this repository
4. Customize your scheduledledger instance by creating your own `config.yaml` file in the scheduledledger folder (see ch. config)

# Config

The configuration of scheduledledger is done in a [yaml](https://yaml.org) file.
Please create the file `config.yaml` for your own configuration. See `defaultconfig.yaml` for all available options and syntax.

Note: You do not need to restart scheduledledger if you change your configuration. It is reloaded periodically.

| Key         | Explanation                                                          |
|-------------|----------------------------------------------------------------------|
| remotename  | name of the rclone remote to which you want to sync your ledger data |
| remotepath  | directory on the remote to which you want to sync your ledger data   |
| currency    | currency used in ledger file                                         |
| transaction | a list of all transactions that should be automatically added        |

A transactions consists of the following elements:

| Key    | Explanation                                               |
|--------|-----------------------------------------------------------|
| rec    | The recipient/payee                                       |
| dom    | the day of month on which the transaction normally occurs |
| amount | the transaction amount                                    |
| from   | the account where the money is subtracted from            |
| to     | the account the money is added to                         |
